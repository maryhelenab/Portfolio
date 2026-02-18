#configura → conecta → cria → instala → testa → apaga


#biblioteca Python que controla AWS
import boto3
#usado para esperar comandos
import time
from botocore.exceptions import ClientError


#Parte 2 — Configurações
REGION = "us-east-1"
AMI_ID = "ami-0e349888043265b96"
INSTANCE_TYPE = "t3.micro"
KEY_NAME = "lab-aws-key"
SECURITY_GROUP_IDS = ["sg-09d8b9296b323c8e5"]

#Conexões com AWS
ec2 = boto3.resource('ec2', region_name=REGION)
ssm = boto3.client('ssm', region_name=REGION)
ec2_client = boto3.client('ec2', region_name=REGION)

#Função criar VM
def launch_instance():
    print("Launching instance...") #"Crie uma VM com essas configurações"
    instances = ec2.create_instances(
        ImageId=AMI_ID,
        MinCount=1,
        MaxCount=1,
        InstanceType= INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SecurityGroupIds=SECURITY_GROUP_IDS,
        IamInstanceProfile={'Name': 'LabInstanceProfile'}, #SSM = AWS Systems Manager
        TagSpecifications=[{
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'lab4-python'}]
        }]
    )
    inst = instances[0]
    inst.wait_until_running() #Script espera a VM ligar antes de continuar.
    inst.reload()
    time.sleep(60) #Isso espera 1 minuto para a VM terminar de inicializar.
    print(f"Launched {inst.id} at {inst.public_ip_address}")
    return inst.id, inst.instance_type, inst.public_ip_address

def run_command_on_instance(instance_id, commands): #Rodar comando dentro da VM
    print(f"Sending SSM command to {instance_id}...")
    resp = ssm.send_command( #SSM Agent dentro da VM — execute isso
        InstanceIds=[instance_id],
        DocumentName="AWS-RunShellScript",
        Parameters={'commands': commands},
        TimeoutSeconds=600, #Depois o script fica verificando o status:
    )
    cmd_id = resp['Command']['CommandId']

    for _ in range(30): #Ele checa a cada 5 segundos se terminou.
        out = ssm.list_command_invocations(CommandId=cmd_id, Details=True)
        if out['CommandInvocations']:
            status = out['CommandInvocations'][0]['Status']
            print("Status:", status)
            if status in ('Failed','TimedOut','Cancelled'):
                print(out)
            else: status = 'Success'
            return
        time.sleep(5)
    raise TimeoutError("Command did not finish in time")

def terminate_instance(instance_id): #Encerrar VM
    print(f"Terminating {instance_id}")
    ec2_client.terminate_instances(InstanceIds=[instance_id])
    waiter = ec2_client.get_waiter('instance_terminated')
    waiter.wait(InstanceIds=[instance_id])#Até ter certeza que foi deletada.
    print("Terminated.")

#execute o script só se ele for rodado diretamente
if __name__ == "__main__":
    iid, _, ip = launch_instance() # Captures the 3 returns
    # Example commands: install nginx and create a file
    cmd_out = run_command_on_instance(iid, [
        "sudo yum update -y || sudo dnf update -y",
        "sudo amazon-linux-extras install -y nginx1 || true", #Isso ativa o repositório correto antes da instalação.
        "sudo yum install -y nginx || sudo dnf install -y nginx",
        "sudo systemctl enable nginx",
        "sudo systemctl start nginx",
        "echo 'Hello from lab4 managed by boto3' | sudo tee /usr/share/nginx/html/index.html"
    ])
    print("Command output (truncated):", cmd_out.get('StandardOutputContent','')
        [:500])
# After validation in browser, terminate:
    terminate_instance(iid)
    
    
        

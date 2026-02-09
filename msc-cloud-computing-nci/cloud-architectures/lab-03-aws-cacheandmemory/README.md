# Lab 03 – AWS Cache and Memory Performance Analysis

**Overview**  
This lab is part of the Master’s Degree in Cloud Computing at NCI and focuses on analyzing cache behavior and memory performance on AWS EC2 instances.

**Objectives**
- Analyze CPU cache hierarchy (L1, L2, L3)
- Measure cache access latency using a Python benchmark
- Evaluate memory throughput using Sysbench
- Understand the relationship between cache size and access latency

**Architecture Overview**  
An AWS EC2 instance running Ubuntu 22.04 was used to execute cache and memory performance tests using Python and Sysbench.

**Technologies and Tools**
- AWS EC2
- Ubuntu 22.04 LTS
- Python 3
- NumPy
- Sysbench

**Description**  
A Python script was used to measure memory access latency for increasing data sizes, revealing cache effects as data exceeds L1, L2, and L3 cache limits.  
Additionally, Sysbench was used to evaluate overall memory throughput and latency under a controlled workload.

**Outputs**
**Outputs**

- Python cache latency test execution  
  ![Cache Test Output](screenshots/07_Cache_Test_Output.png.jpg)

- Cache latency results for increasing memory sizes  
  ![Cache Latency](screenshots/07_Cache_Test_Output.png.jpg)

- CPU cache hierarchy information  
  ![Cache Information](screenshots/05_CPU_Cache_and_Memory_Info.png.jpg)

- Python and Sysbench version verification  
  ![Versions](screenshots/04_Python_Sysbench_Version.png.jpg)

- NumPy installation confirmation  
  ![NumPy Installed](screenshots/08_NumPy_Installation.png.jpg)

- Cache test Python script  
  ![Cache Test Script](screenshots/06_Cache_Test_Code.png.jpg)

- Memory throughput benchmark using Sysbench  
  ![Sysbench Memory Test](screenshots/10_Sysbench_Memory_Test.png.jpg)


**Learning Outcomes**
- Understanding CPU cache hierarchy and behavior
- Measuring cache latency and memory throughput
- Observing cache performance impact on memory access
- Using benchmarking tools in cloud environments

**Conclusion**  
This lab demonstrated how cache size and memory hierarchy significantly affect application performance.  
The experiments highlight the importance of cache-aware programming and memory benchmarking when designing high-performance applications in cloud environments.

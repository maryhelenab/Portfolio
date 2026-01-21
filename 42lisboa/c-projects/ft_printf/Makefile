# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: maryhelen <maryhelen@student.42.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/12/08 18:26:59 by malbuque          #+#    #+#              #
#    Updated: 2021/12/26 11:07:53 by maryhelen        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = 		libftprintf.a
#Nome do project

SRCS = 		ft_printf.c \
			ft_check_arg.c \
			ft_putchar.c \
			ft_putstr.c \
			ft_pointer.c \
			ft_strlen.c \
			ft_base.c #\
			ft_printf_utils_char.c \
			ft_printf_utils_hex.c \
			ft_printf_utils_num.c \
			ft_printf_utils.c

#Objs arquivos transforma .c (files) em .o (objtos)
OBJS = 		$(SRCS:.c=.o)

CC			= gcc
CFLAGS		= -Wall -Wextra -Werror -I.
# -I (incluir) Especifica um diretório para pesquisar os makefiles incluídos
RM			= rm -f
# -rm remover arquivos tudo de raiz
# -f ignore arquivos e argumentos inexistentes, nunca pergunte

all: $(NAME)

$(NAME): $(OBJS)
	ar rcs $(NAME) $(OBJS)
# ar cria e mantém arquivos de arquivos. 
# r significa que, se a biblioteca já existir, substitua os arquivos antigos da biblioteca pelos novos. 
# c significa criar a biblioteca se ela não existir. 
# s pode significar 'classificar' (criar um índice classificado) da biblioteca, para que seja indexada e 
    # mais rapidamente para acessar as funções na biblioteca. 
# Portanto, rcs pode ser visto como significando replace, create, sort.
clean:
	$(RM) $(OBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

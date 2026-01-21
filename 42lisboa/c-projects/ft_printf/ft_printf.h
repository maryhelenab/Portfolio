/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: maryhelen <maryhelen@student.42.fr>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/12/08 18:31:06 by malbuque          #+#    #+#             */
/*   Updated: 2022/01/14 16:30:10 by maryhelen        ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdio.h>
# include <unistd.h>
# include <stdarg.h>

int		ft_printf(const char *format, ...);
int		ft_check_arg(char c, va_list args);
int		ft_putchar(char c, int i);
int		ft_putstr(const void *str);
int		ft_pointer(unsigned long int nbr);
int		ft_strlen(const char *s);
int		ft_base(long long int nbr, char *base);

#endif

import interpolations as ip

#Interpolacja Lagrange'a - różne rozmieszczenia punktów

ip.generate_plot("sopot", "lagrange",10,"even")
ip.generate_plot("sopot", "lagrange",10,"random")
ip.generate_plot("sopot", "lagrange",10,"chebyshev")

#Interpolacja Lagrange'a - różne liczby punktów

ip.generate_plot("sopot", "lagrange",5,"even")
ip.generate_plot("sopot", "lagrange",15,"even")
ip.generate_plot("sopot", "lagrange",25,"even")

ip.generate_plot("sopot", "lagrange",5,"chebyshev")
ip.generate_plot("sopot", "lagrange",15,"chebyshev")
ip.generate_plot("sopot", "lagrange",25,"chebyshev")

#Interpolacja Lagrange'a - różne charaktery tras

ip.generate_plot("beskid", "lagrange",15,"even")
ip.generate_plot("beskid", "lagrange",15,"chebyshev")
ip.generate_plot("beskid", "lagrange",20,"chebyshev")

ip.generate_plot("poznan", "lagrange",15,"even")
ip.generate_plot("poznan", "lagrange",15,"chebyshev")
ip.generate_plot("poznan", "lagrange",20,"chebyshev")

ip.generate_plot("jaroslawiec", "lagrange",15,"even")
ip.generate_plot("jaroslawiec", "lagrange",15,"chebyshev")
ip.generate_plot("jaroslawiec", "lagrange",40,"chebyshev")


#Interpolacja splajnami różne rozmieszczenia punktów

ip.generate_plot("sopot", "spline",10,"even")
ip.generate_plot("sopot", "spline",10,"random")
ip.generate_plot("sopot", "spline",10,"chebyshev")

#Interpolacja splajnami - różne liczby punktów

ip.generate_plot("sopot", "spline",5,"even")
ip.generate_plot("sopot", "spline",15,"even")
ip.generate_plot("sopot", "spline",25,"even")

#Interpolacja splajnami - różne charaktery tras

ip.generate_plot("beskid", "spline",10,"even")
ip.generate_plot("beskid", "spline",20,"even")

ip.generate_plot("poznan", "spline",10,"even")
ip.generate_plot("poznan", "spline",20,"even")

ip.generate_plot("jaroslawiec", "spline",10,"even")
ip.generate_plot("jaroslawiec", "spline",20,"even")
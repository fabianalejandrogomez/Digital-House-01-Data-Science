#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def modales_decorador(funcion):
    
    def fun_wrapper():
        # Código antes de la función
        print('Por favor')
        funcion()
        # Código despues de la función
        print('Gracias')
    
    return fun_wrapper


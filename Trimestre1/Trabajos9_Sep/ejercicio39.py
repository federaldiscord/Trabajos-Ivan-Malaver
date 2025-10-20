import json
import os

ESCENAS = {
    'inicio': {
        'texto': "Te despiertas en la entrada de la aldea de Liria. Un camino hacia el bosque al norte y una posada a la derecha.",
        'opciones': {
            'n': {
                'descripcion': 'Ir al bosque',
                'siguiente': 'bosque',
                'efectos': {}
            },
            'd': {
                'descripcion': 'Entrar a la posada',
                'siguiente': 'posada',
                'efectos': {}
            },
            'mirar': {
                'descripcion': 'Mirar alrededor',
                'siguiente': 'inicio',
                'efectos': {'add_item': 'mapa'}
            }
        }
    },

    'posada': {
        'texto': "La posada huele a pan y cerveza. El tabernero te ofrece trabajo: escoltar una caravana (recompensa).",
        'opciones': {
            'aceptar': {
                'descripcion': 'Aceptar el trabajo (recompensa: moneda)',
                'siguiente': 'caravana',
                'efectos': {'add_item': 'moneda'}
            },
            'rechazar': {
                'descripcion': 'Rechazar y volver a la entrada',
                'siguiente': 'inicio',
                'efectos': {}
            }
        }
    },

    'bosque': {
        'texto': "En el bosque encuentras un sendero y una cueva oscura. Se escuchan ruidos.",
        'opciones': {
            'sendero': {
                'descripcion': 'Seguir el sendero',
                'siguiente': 'claro',
                'efectos': {}
            },
            'cueva': {
                'descripcion': 'Explorar la cueva',
                'siguiente': 'cueva',
                'efectos': {}
            },
            'volver': {
                'descripcion': 'Volver a la aldea',
                'siguiente': 'inicio',
                'efectos': {}
            }
        }
    },

    'claro': {
        'texto': "Llegas a un claro donde un lobo te embosca.",
        'opciones': {
            'pelear': {
                'descripcion': 'Pelear con el lobo',
                'siguiente': 'claro_post',
                'efectos': {'change_health': -4, 'add_item': 'piel_lobo'}
            },
            'huir': {
                'descripcion': 'Huir hacia la aldea (pierdes salud)',
                'siguiente': 'inicio',
                'efectos': {'change_health': -2}
            }
        }
    },

    'claro_post': {
        'texto': "Sobrevives a la pelea. Puedes abrirte paso hacia una torre al este o volver.",
        'opciones': {
            'este': {
                'descripcion': 'Ir a la torre',
                'siguiente': 'torre',
                'efectos': {}
            },
            'volver': {
                'descripcion': 'Regresar a la aldea',
                'siguiente': 'inicio',
                'efectos': {}
            }
        }
    },

    'cueva': {
        'texto': "Dentro de la cueva hay un cofre cerrado con una cerradura vieja.",
        'opciones': {
            'forzar': {
                'descripcion': 'Forzar el cofre (riesgo)',
                'siguiente': 'cueva_forzada',
                'efectos': {'change_health': -3, 'add_item': 'anillo'}
            },
            'buscar_llave': {
                'descripcion': 'Buscar llave en la cueva',
                'siguiente': 'cueva_llave',
                'efectos': {'add_item': 'llave'}
            },
            'salir': {
                'descripcion': 'Salir de la cueva',
                'siguiente': 'bosque',
                'efectos': {}
            }
        }
    },

    'cueva_llave': {
        'texto': "Encuentras una llave oxidada entre las rocas.",
        'opciones': {
            'abrir': {
                'descripcion': 'Abrir el cofre con la llave',
                'siguiente': 'cueva_abierta',
                'requisitos': {'require_item': 'llave'},
                'efectos': {'add_item': 'espada'}
            },
            'volver': {
                'descripcion': 'Volver',
                'siguiente': 'cueva',
                'efectos': {}
            }
        }
    },

    'cueva_forzada': {
        'texto': "Forzaste el cofre y encontraste un anillo misterioso, pero sufriste heridas.",
        'opciones': {
            'inspeccionar': {
                'descripcion': 'Inspeccionar el anillo',
                'siguiente': 'anillo',
                'efectos': {}
            },
            'salir': {
                'descripcion': 'Salir de la cueva',
                'siguiente': 'bosque',
                'efectos': {}
            }
        }
    },

    'cueva_abierta': {
        'texto': "Dentro encuentras una espada afilada.",
        'opciones': {
            'tomar': {
                'descripcion': 'Tomar la espada',
                'siguiente': 'cueva',
                'efectos': {'add_item': 'espada'}
            },
            'salir': {
                'descripcion': 'Salir',
                'siguiente': 'bosque',
                'efectos': {}
            }
        }
    },

    'anillo': {
        'texto': "El anillo brilla y te susurra: 'Protección'. Te sientes más fuerte.",
        'opciones': {
            'seguir': {
                'descripcion': 'Seguir',
                'siguiente': 'bosque',
                'efectos': {'set_flag': 'anillo_activo'}
            }
        }
    },

    'torre': {
        'texto': "La torre está custodiada por un guardián que exige un pago o demostrar fuerza.",
        'opciones': {
            'pagar': {
                'descripcion': 'Pagar con moneda',
                'siguiente': 'interior_torre',
                'requisitos': {'require_item': 'moneda'},
                'efectos': {'remove_item': 'moneda'}
            },
            'pelear': {
                'descripcion': 'Pelear con el guardián (mejor si tienes espada)',
                'siguiente': 'pelea_guardian',
                'efectos': {'change_health': -5}
            },
            'volver': {
                'descripcion': 'Volver',
                'siguiente': 'claro_post',
                'efectos': {}
            }
        }
    },

    'pelea_guardian': {
        'texto': "El guardián es fuerte. Si tienes espada tus heridas son menores.",
        'opciones': {
            'seguir': {
                'descripcion': 'Continuar',
                'siguiente': 'interior_torre',
                'requisitos': {},
                'efectos': {}
            }
        }
    },

    'interior_torre': {
        'texto': "Dentro de la torre hay un cofre final. Puedes abrirlo si posees la espada o el anillo.",
        'opciones': {
            'abrir': {
                'descripcion': 'Abrir el cofre final',
                'siguiente': 'final_tesoro',
                'requisitos': {'one_of_items': ['espada', 'anillo']},
                'efectos': {}
            },
            'salir': {
                'descripcion': 'Salir',
                'siguiente': 'torre',
                'efectos': {}
            }
        }
    },

    'final_tesoro': {
        'texto': "Has abierto el cofre final: ¡Riquezas y gloria! FIN (Victoria)",
        'opciones': {}
    },

    'muerte': {
        'texto': "Has perdido toda tu salud y sucumbiste a tus heridas. FIN (Muerte)",
        'opciones': {}
    }
}

class Juego:
    def __init__(self, escenas):
        self.escenas = escenas
        self.estado = {
            'salud': 10,
            'inventario': set(),
            'escena': 'inicio',
            'flags': set()
        }

    def cumple_requisitos(self, requisitos):
        if not requisitos:
            return True
        if 'require_item' in requisitos:
            if requisitos['require_item'] not in self.estado['inventario']:
                return False
        if 'min_salud' in requisitos:
            if self.estado['salud'] < requisitos['min_salud']:
                return False
        if 'flag_set' in requisitos:
            if requisitos['flag_set'] not in self.estado['flags']:
                return False
        if 'one_of_items' in requisitos:
            if not any(item in self.estado['inventario'] for item in requisitos['one_of_items']):
                return False
        return True

    def aplicar_efectos(self, efectos):
        if not efectos:
            return
        if 'add_item' in efectos:
            item = efectos['add_item']
            self.estado['inventario'].add(item)
            print(f"-> Obtuviste: {item}")
        if 'remove_item' in efectos:
            item = efectos['remove_item']
            if item in self.estado['inventario']:
                self.estado['inventario'].remove(item)
                print(f"-> Se removió: {item}")
        if 'change_health' in efectos:
            delta = efectos['change_health']
            self.estado['salud'] += delta
            print(f"-> Salud {'+' if delta>=0 else ''}{delta} (ahora {self.estado['salud']})")
        if 'set_flag' in efectos:
            flag = efectos['set_flag']
            self.estado['flags'].add(flag)
            print(f"-> Bandera activada: {flag}")

    def mostrar_estado(self):
        inv = ', '.join(self.estado['inventario']) if self.estado['inventario'] else 'vacío'
        flags = ', '.join(self.estado['flags']) if self.estado['flags'] else 'ninguna'
        print(f"\n-- Estado --\nSalud: {self.estado['salud']}\nInventario: {inv}\nFlags: {flags}\nEscena: {self.estado['escena']}")

    def guardar(self, ruta='guardado_juego.json'):
        data = {
            'salud': self.estado['salud'],
            'inventario': list(self.estado['inventario']),
            'escena': self.estado['escena'],
            'flags': list(self.estado['flags'])
        }
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Juego guardado en {ruta}")

    def cargar(self, ruta='guardado_juego.json'):
        if not os.path.exists(ruta):
            print('No existe archivo de guardado')
            return
        with open(ruta, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.estado['salud'] = data.get('salud', 10)
        self.estado['inventario'] = set(data.get('inventario', []))
        self.estado['escena'] = data.get('escena', 'inicio')
        self.estado['flags'] = set(data.get('flags', []))
        print('Juego cargado')

    def jugar(self):
        print('INICIANDO JUEGO DE AVENTURA')
        while True:
            if self.estado['salud'] <= 0:
                print('\nHas quedado sin salud.')
                self.estado['escena'] = 'muerte'

            escena_id = self.estado['escena']
            escena = self.escenas.get(escena_id)
            if escena is None:
                print('Escena inexistente, terminando juego.')
                break

            print('\n' + '-'*40)
            print(escena.get('texto', ''))

            opciones = escena.get('opciones', {})
            if not opciones:
                print('\n--- Fin de la escena ---')
                break

            disponibles = {}
            for clave, opt in opciones.items():
                req = opt.get('requisitos', {})
                if self.cumple_requisitos(req):
                    disponibles[clave] = opt

            print('\nOpciones:')
            for k, opt in disponibles.items():
                print(f" {k} -> {opt['descripcion']}")
            print("Comandos: estado, guardar, cargar, ayuda, reiniciar, salir")

            cmd = input('> ').strip().lower()
            if cmd in ('salir', 'q'):
                print('Saliendo del juego...')
                break
            if cmd == 'estado':
                self.mostrar_estado(); continue
            if cmd == 'guardar':
                self.guardar(); continue
            if cmd == 'cargar':
                self.cargar(); continue
            if cmd == 'ayuda':
                print('Escribe la clave de la opción para elegirla. Usa comandos globales.'); continue
            if cmd == 'reiniciar':
                self.__init__(self.escenas); print('Juego reiniciado.'); continue

            if cmd not in disponibles:
                print('Opción no válida o no disponible por requisitos.')
                continue

            opcion = disponibles[cmd]
            efectos = opcion.get('efectos', {})
            self.aplicar_efectos(efectos)
            siguiente = opcion.get('siguiente')
            if siguiente:
                self.estado['escena'] = siguiente

        print('\nFIN DEL JUEGO')

if __name__ == '__main__':
    juego = Juego(ESCENAS)
    juego.jugar()
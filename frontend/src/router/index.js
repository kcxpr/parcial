import Vue from 'vue'
import VueRouter from 'vue-router'
import Videojuego from '@/components/videojuego'
import Videojuego1 from '@/components/insertar'
import Videojuego2 from '@/components/actualizar'
Vue.use(VueRouter)

const routes = [  
  {
    path: '/videojuegos/lista',
    name: 'Videojuego',
    component: Videojuego
  },
  {
    path: '/insertar',
    name: 'Videojuego insertar',
    component:Videojuego1
  },
  {
    path: '/actualizar/:id/:name/:notes',
    name: 'Videojuego actualizar',
    component: Videojuego2
  },
]

const router = new VueRouter({
  routes: routes,
  mode: 'history',
})
export default router

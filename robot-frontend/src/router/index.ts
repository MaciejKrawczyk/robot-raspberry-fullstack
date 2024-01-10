import { createRouter, createWebHistory } from 'vue-router'

import { type IStaticMethods } from "preline/preline";
import Manual from "@/views/Manual.vue";
declare global {
  interface Window {
    HSStaticMethods: IStaticMethods;
  }
}

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'manual',
      component: Manual
    },
    {
      path: '/program',
      name: 'program',
      component: () => import('../views/Program.vue')
    },
    {
      path: '/registry',
      name: 'registry',
      component: () => import('../views/Registry.vue')
    }
  ]
})

router.afterEach((to, from, failure) => {
  if (!failure) {
    setTimeout(() => {
      window.HSStaticMethods.autoInit();
    }, 100)
  }
});

export default router

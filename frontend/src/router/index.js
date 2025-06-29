import { createRouter, createWebHistory } from 'vue-router';
import DashboardView from '@/views/DashboardView.vue';
import ProjectsView from '@/views/ProjectsView.vue';
import AiPmView from '@/views/AiPmView.vue';

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: DashboardView,
    meta: {
      title: 'Dashboard - 一键升级-uplus'
    }
  },
  {
    path: '/projects',
    name: 'Projects',
    component: ProjectsView,
    meta: {
      title: 'Projects - 一键升级-uplus'
    }
  },
  {
    path: '/ai-pm',
    name: 'AiPm',
    component: AiPmView,
    meta: {
      title: 'AI Product Manager - 一键升级-uplus'
    }
  },
  {
    path: '/rsd',
    name: 'RSD',
    component: () => import('@/views/RsdView.vue'),
    meta: {
      title: 'RSD Documents - 一键升级-uplus'
    }
  },
  {
    path: '/bitcup',
    name: 'Bitcup',
    component: () => import('@/views/BitcupView.vue'),
    meta: {
      title: 'BITCUP Models - 一键升级-uplus'
    }
  },
  // Redirect any unmatched routes to home
  {
    path: '/:pathMatch(.*)*',
    redirect: '/'
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } else {
      return { top: 0 };
    }
  }
});

// Update document title based on route meta
router.beforeEach((to, from, next) => {
  document.title = to.meta.title || '一键升级-uplus';
  next();
});

export default router;
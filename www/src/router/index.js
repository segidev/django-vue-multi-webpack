import Vue from 'vue'
import Router from 'vue-router'
import Coop from "../components/Coop"
import Person from "company-person-module/src/components/Person"
import Events from "company-events-module/src/components/Events"

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Coop',
      component: Coop
    },
    {
      path: '/person',
      name: 'Person',
      component: Person
    },
    {
      path: '/events',
      name: 'Events',
      component: Events
    },
  ]
})

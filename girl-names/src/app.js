import Vue from 'vue'
import App from './App.vue'

import { createRouter } from './router/router'
import { createStore } from './store/store'
import './components'

import { sync } from 'vuex-router-sync'


import * as ssr_window from 'ssr-window'

  // import document from 'ssr-windo'
  if (typeof window === 'undefined') {
    global.window = ssr_window.window
}
if (typeof document === 'undefined') {
    global.document = ssr_window.document
}

if (typeof global.navigator === 'undefined'){
global.navigator = {
  userAgent: 'node',
}
}




// export a factory function for creating fresh app, router and store
// instances
export function createApp () {

  const store = createStore()
  const router = createRouter()

  sync(store, router)

  const app = new Vue({
    // the root instance simply renders the App component.
    router,
    store,
    render: h => h(App)
  })
  return { app, router, store }
}

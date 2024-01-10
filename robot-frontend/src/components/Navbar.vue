<template>


  <div class="border-t-2 border-gray-200 dark:border-gray-700 fixed bottom-0 w-full">

    <nav class="-mb-0.5 flex justify-around space-x-6">

      <router-link
          class="py-4 px-1 inline-flex items-center gap-2 border-b-2 border-transparent text-sm whitespace-nowrap text-gray-500 hover:text-blue-600 focus:outline-none focus:text-blue-600"
          to="/"
      >
        Manual
      </router-link>

      <router-link
          class="py-4 px-1 inline-flex items-center gap-2 border-b-2 border-transparent text-sm whitespace-nowrap text-gray-500 hover:text-blue-600 focus:outline-none focus:text-blue-600"
          to="/program"
      >
        Program
      </router-link>

      <router-link
          class="py-4 px-1 inline-flex items-center gap-2 border-b-2 border-transparent text-sm whitespace-nowrap text-gray-500 hover:text-blue-600 focus:outline-none focus:text-blue-600"
          to="/registry"
      >
        Registry
      </router-link>

    </nav>

  </div>


</template>


<script lang="ts">


export default {
  name: 'NavbarApp',
  setup() {


  }
}

</script>
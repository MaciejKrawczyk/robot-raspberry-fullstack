<template>

  <div class="w-64 flex flex-col justify-center items-center p-1">
    <h2>{{ name }}</h2>
    <div class="flex">
      <button
          type="button"
          class="py-3 px-4 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none">
        -
      </button>
      <input
          type="text"
          class="text-center py-3 px-4 block w-32 border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none "
          :placeholder="value"
          readonly>
      <button
          type="button"
          class="py-3 px-4 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none">
        +
      </button>
    </div>
  </div>

</template>

<script setup lang="ts">
import {ref} from 'vue';

// Define props
const props = defineProps({
  name: String,
  value: String,
});

// Use the props in your component
const name = ref(props.name);
const value = ref(props.value);
</script>

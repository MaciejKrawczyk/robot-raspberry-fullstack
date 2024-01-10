<template>

  <position-manual-setting name="theta1" :value="theta1"/>

  <position-manual-setting name="theta2" :value="theta2"/>

  <position-manual-setting name="theta3" :value="theta3"/>

  <position-manual-setting name="x" value="0"/>

  <position-manual-setting name="y" value="0"/>

  <position-manual-setting name="z" value="0"/>

  <button
      type="button"
      class="my-10 mx-5 py-3 px-4 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
      @click.prevent="savePosition"
  >

    Save position
  </button>

</template>

<script setup lang="ts">
import {ref} from 'vue';
import PositionManualSetting from "@/components/PositionManualSetting.vue";

const theta1 = ref(0);
const theta2 = ref(0);
const theta3 = ref(0);

const savePosition = async () => {
  try {
    await fetch('http://localhost:5000/position', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        theta1: theta1.value,
        theta2: theta2.value,
        theta3: theta3.value,
      })
    });
  } catch (error) {
    console.error('Failed to save position:', error);
  }
};
</script>
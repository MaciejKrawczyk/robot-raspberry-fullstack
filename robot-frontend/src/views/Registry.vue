<template>
  <div class="flex flex-col">
    <div class=" overflow-x-auto">
      <div class=" min-w-full inline-block align-middle">
        <div class="overflow-hidden">
          <table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
            <thead>
            <tr>
              <th scope="col" class="px-6 py-3 text-center text-xs font-medium text-gray-500 uppercase">ID</th>
              <th scope="col" class="px-6 py-3 text-center text-xs font-medium text-gray-500 uppercase">theta1</th>
              <th scope="col" class="px-6 py-3 text-center text-xs font-medium text-gray-500 uppercase">theta2</th>
              <th scope="col" class="px-6 py-3 text-center text-xs font-medium text-gray-500 uppercase">theta3</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(item, index) in data" :key="index"
                class="odd:bg-white even:bg-gray-100">
              <td class="px-6 py-4 text-center whitespace-nowrap text-sm font-medium text-gray-800">
                {{ item.id }}
              </td>
              <td class="px-6 py-4 text-center whitespace-nowrap text-sm text-gray-800">
                {{ item.theta1 }}
              </td>
              <td class="px-6 py-4 text-center whitespace-nowrap text-sm text-gray-800">
                {{ item.theta2 }}
              </td>
              <td class="px-6 py-4 text-center whitespace-nowrap text-sm text-gray-800">
                {{ item.theta3 }}
              </td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import {onMounted, reactive} from 'vue';

const data = reactive<{ id: number, theta1: number, theta2: number, theta3: number }[]>([]);

onMounted(async () => {
  try {
    const response = await fetch('http://localhost:5000/position');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const positions = await response.json();
    if (!Array.isArray(positions)) {
      throw new Error('Fetched data is not an array');
    }
    data.push(...positions);
  } catch (error) {
    console.error('Fetch failed:', error);
  }
});
</script>
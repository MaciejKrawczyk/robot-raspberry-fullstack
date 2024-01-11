<template>

  <div class="w-auto mx-10 my-10 h-auto bg-gray-800 text-white">

    <div class="w-full h-14 bg-slate-700">
      <button
          :disabled="isDisabled"
          type="button"
          class="py-2 px-3 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
      >
        RUN
      </button>
    </div>

    <table class="text-lg font-mono m-10">
      <tbody>
      <tr
          class=""
          v-for="(command, index) in commands"
          :key="command.id"
      >
        <td class="w-14 text-gray-400">
          {{ index + 1 }}
        </td>
        <td class="border-l-2 border-gray-400 pl-4 pr-20">
          <p>
            {{ commandTypes[command.command_type].display(command.position_id) }}
          </p>
        </td>
        <td>
          <button
              type="button"
              class="py-2 px-3 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
              @click.prevent="deleteCommand(command.id)"
          >
            X
          </button>
        </td>
      </tr>
      </tbody>
    </table>

    <div class="flex">

      <!-- Floating Select -->
      <div class="relative">
        <select
            v-model="selectedCommandType"
            class="peer p-4 pe-9 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600
        focus:pt-6
        focus:pb-2
        [&:not(:placeholder-shown)]:pt-6
        [&:not(:placeholder-shown)]:pb-2
        autofill:pt-6
        autofill:pb-2">
          <!--        <option selected>Command type</option>-->
          <option v-for="commandType in commandTypesList" :key="commandType">{{ commandType }}</option>
        </select>
        <label class="absolute top-0 start-0 p-4 h-full truncate pointer-events-none transition ease-in-out duration-100 border border-transparent dark:text-white peer-disabled:opacity-50 peer-disabled:pointer-events-none
      peer-focus:text-xs
      peer-focus:-translate-y-1.5
      peer-focus:text-gray-500
      peer-[:not(:placeholder-shown)]:text-xs
      peer-[:not(:placeholder-shown)]:-translate-y-1.5
      peer-[:not(:placeholder-shown)]:text-gray-500">type</label>
      </div>
      <!-- End Floating Select -->

      <!-- Floating Select -->
      <div class="relative">
        <select
            v-model="selectedPositionId"
            :disabled="selectedCommandType === 'sleep'"
            class="peer p-4 pe-9 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600
        focus:pt-6
        focus:pb-2
        [&:not(:placeholder-shown)]:pt-6
        [&:not(:placeholder-shown)]:pb-2
        autofill:pt-6
        autofill:pb-2">
          <!--        <option selected>Position ID</option>-->
          <option v-for="position in positions" :key="position.id">
            <!--          {{position.id}}-->
            {{ position.id }} -> θ1: {{ position.theta1 }}, θ2: {{ position.theta2 }}, θ3: {{ position.theta3 }}
          </option>
        </select>
        <label class="absolute top-0 start-0 p-4 h-full truncate pointer-events-none transition ease-in-out duration-100 border border-transparent dark:text-white peer-disabled:opacity-50 peer-disabled:pointer-events-none
      peer-focus:text-xs
      peer-focus:-translate-y-1.5
      peer-focus:text-gray-500
      peer-[:not(:placeholder-shown)]:text-xs
      peer-[:not(:placeholder-shown)]:-translate-y-1.5
      peer-[:not(:placeholder-shown)]:text-gray-500">position</label>
      </div>
      <!-- End Floating Select -->

      <button
          :disabled="isDisabled"
          type="button"
          class="py-2 px-3 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
          @click.prevent="sendCommand(selectedCommandType, selectedPositionId)"
      >
        +
      </button>

    </div>

  </div>

</template>


<script setup lang="ts">

const commandTypeString = "Command type"
const positionIdString = "Position ID"

import {onMounted, reactive, ref} from 'vue';

interface Command {
  id: number;
  command_type: string
  position_id: any
  previous_id: number;
  next_id: number;
}

const commandTypes = {
  sleep: {
    display: (position) => {
      return "sleep(1)"
    }
  },
  move: {
    display: (position: string) => {
      return `moveTo(registry(${position}));`
    }
  }
}

const selectedPositionId = ref(positionIdString)
const selectedCommandType = ref(commandTypeString)
const commandTypesList = Object.keys(commandTypes)

const commands = reactive<Command[]>([]);
const positions = reactive([])
let isDisabled = ref(false)

const deleteCommand = async (id: number) => {
  try {
    const response = await fetch(`http://localhost:5000/command/${id}`, {
      method: 'DELETE',
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    // Refresh the list of commands
    await fetchCommands();
  } catch (error) {
    console.error('Delete failed:', error);
  }
};

const fetchCommands = async () => {
  try {
    const response = await fetch('http://localhost:5000/command');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const fetchedCommands = await response.json();
    if (!Array.isArray(fetchedCommands)) {
      throw new Error('Fetched data is not an array');
    }
    commands.splice(0, commands.length, ...fetchedCommands);
  } catch (error) {
    console.error('Fetch failed:', error);
  }
};

const fetchPositions = async () => {
  try {
    const response = await fetch('http://localhost:5000/position');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const fetchedPositions = await response.json();
    if (!Array.isArray(fetchedPositions)) {
      throw new Error('Fetched data is not an array');
    }
    positions.splice(0, commands.length, ...fetchedPositions);
  } catch (error) {
    console.error('Fetch failed:', error);
  }
};

const sendCommand = async (commandType: string, positionId: any) => {

  try {

    isDisabled.value = true

    if (commandType === commandTypeString) {
      // console.log('stop')
      alert("Choose correct command type!")
      return
    }

    if (commandType === commandTypeString && positionId !== positionIdString) {
      // console.log('stop')
      alert("invalid input!")
      return
    }

    if (commandType === 'move' && positionId === positionIdString) {
      // console.log('stop')
      alert("Choose correct position id!")
      return
    }


    if (positionId === positionIdString && commandType === commandTypeString) {
      // console.log('stop')
      alert("invalid input!")
      return
    }

    const response = await fetch('http://localhost:5000/command', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        command_type: commandType,
        position_id: positionId[0] || null,
      }),
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
  } catch (error) {
    console.error('POST request failed:', error);
  } finally {
    await fetchCommands()
    isDisabled.value = false
  }
};

onMounted(fetchCommands);
onMounted(fetchPositions)

</script>
<template>
    <div class="w-full flex flex-col max-w-sm bg-gray-100 rounded-lg shadow-md p-6 mx-auto">
        <h2 class="text-2xl font-bold text-gray-800 mb-4 text-center">Add a new Task!</h2>
        <form @submit.prevent="addNewTask">
            <div class="flex mb-4 justify-between">
                <label class="text-sm font-medium text-gray-700">Mode
                    <select v-model.trim="mode"
                        class="ml-1 focus:outline-none focus:ring-2 focus:ring-indigo-500 border-gray-300 rounded-md shadow-sm"
                        required>
                        <option value="private">Private</option>
                        <option value="team">Team</option>
                    </select>
                </label>

                <label class="text-sm font-medium text-gray-700">Priority
                    <select v-model.trim="priority"
                        :class="priority === 'high'
                            ? 'text-red-500 ml-1 focus:outline-none focus:ring-2 focus:ring-indigo-500 border-gray-300 rounded-md shadow-sm'
                            : 'ml-1 focus:outline-none focus:ring-2 focus:ring-indigo-500 border-gray-300 rounded-md shadow-sm'" required>
                        <option value="high">High</option>
                        <option value="medium" class="text-gray-700">Medium</option>
                        <option value="medium" class="text-gray-700">Low</option>
                    </select>
                </label>
            </div>

            <div class="flex mb-4 justify-between">
                <label class="text-sm font-medium text-gray-700">Topic
                    <select v-model.trim="topic"
                        class="ml-1 focus:outline-none focus:ring-2 focus:ring-indigo-500 border-gray-300 rounded-md shadow-sm"
                        required>
                        <option value="shopping">Shopping</option>
                        <option value="housework">Housework</option>
                    </select>
                </label>

                <label class="text-sm font-medium text-gray-700">Category
                    <select v-model.trim="category"
                        class="ml-1 focus:outline-none focus:ring-2 focus:ring-indigo-500 border-gray-300 rounded-md shadow-sm"
                        required>
                        <option value="default">Default</option>
                        <option value="timed">Timed</option>
                        <option value="recurring">Recurring</option>
                    </select>
                </label>
            </div>

            <div :class="category === 'timed' ? 'mb-4' : 'hidden mb-4'">
                <label class="text-sm font-medium text-gray-700">Deadline
                    <input v-model.trim="deadlineDate" type="date" required
                        class="mt-1 w-fit px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
                </label>
            </div>

            <div :class="category === 'recurring' ? 'mb-4' : 'hidden mb-4'">
                <label class="text-sm font-medium text-gray-700">Interval
                    <select v-model.trim="interval"
                        class="ml-1 focus:outline-none focus:ring-2 focus:ring-indigo-500 border-gray-300 rounded-md shadow-sm"
                        required>
                        <option value="daily">Daily</option>
                        <option value="weekly">Weekly</option>
                        <option value="monthly">Monthly</option>
                    </select>
                </label>
            </div>

            <div :class="interval === 'weekly' | interval === 'monthly' ? 'mb-4' : 'hidden mb-4'">
                <label class="text-sm font-medium text-gray-700">Start Date
                    <input v-model.trim="startDate" type="date" required
                        class="mt-1 w-fit px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
                </label>
            </div>

            <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700">Title
                    <input v-model.trim="title" type="text" required
                        class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
                </label>
            </div>

            <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700">Description
                    <textarea v-model.trim="description" type="text" required
                        class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
                </label>
            </div>

            <div class="w-full flex justify-between">
                <button type="reset"
                    class="w-fit bg-indigo-600 text-white py-1 px-4 rounded-md hover:bg-indigo-800 transition">Reset</button>
                <button type="submit"
                    class="w-fit bg-indigo-600 text-white py-1 px-2 rounded-md hover:bg-indigo-800 transition">Submit</button>
            </div>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue';

let id = 0  // Replace with ref() later!

const mode = ref('')
const priority = ref('')
const category = ref('')
const topic = ref('')
const deadlineDate = ref('')
const interval = ref('')
const startDate = ref('')
const title = ref('')
const description = ref('')

const addNewTask = () => {
    id = id + 1

    const newTask = {
        id,
        title: title.value,
        mode: mode.value,
        category: category.value,
        priority: priority.value,
        deadlineDate: deadlineDate.value,
        remainingTime: remainingTime.value,
        description: description.value
    }

    console.log('Adding new task: ', newTask);
}
</script>
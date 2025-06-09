<template>
    <div class="w-full flex flex-col max-w-sm bg-gray-100 rounded-lg shadow-md p-6 mx-auto">
        <!-- Task-Form-Header -->
        <h2 class="text-2xl font-bold text-gray-800 mb-4 text-center">Add a new Task!</h2>

        <!-- Message-Box -->
        <message-box :msg="msg" :errorPhrase="errorPhrase"></message-box>

        <!-- Task-Form -->
        <form @submit.prevent="submitNewTask">
            <!-- Mode -->
            <div class="flex mb-4 justify-between">
                <label class="text-sm font-medium text-gray-700">Mode
                    <select v-model.trim="mode"
                        class="ml-1 focus:outline-none focus:ring-2 focus:ring-indigo-500 border-gray-300 rounded-md shadow-sm"
                        required>
                        <option value="private">Private</option>
                        <option value="team">Team</option>
                    </select>
                </label>

                <!-- Priority -->
                <label class="text-sm font-medium text-gray-700">Priority
                    <select v-model.trim="priority"
                        :class="priority === 'high'
                            ? 'text-red-600 ml-1 focus:outline-none focus:ring-2 focus:ring-indigo-500 border-gray-300 rounded-md shadow-sm'
                            : 'ml-1 focus:outline-none focus:ring-2 focus:ring-indigo-500 border-gray-300 rounded-md shadow-sm'" required>
                        <option value="high">High</option>
                        <option value="medium" class="text-gray-700">Medium</option>
                        <option value="low" class="text-gray-700">Low</option>
                    </select>
                </label>
            </div>

            <!-- Topic -->
            <div class="flex mb-4 justify-between">
                <label class="text-sm font-medium text-gray-700">Topic
                    <select v-model.trim="topic"
                        class="ml-1 focus:outline-none focus:ring-2 focus:ring-indigo-500 border-gray-300 rounded-md shadow-sm"
                        required>
                        <option value="shopping">Shopping</option>
                        <option value="housework">Housework</option>
                    </select>
                </label>

                <!-- Category -->
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

            <!-- Deadline -->
            <div :class="category === 'timed' ? 'mb-4' : 'hidden'">
                <label class="text-sm font-medium text-gray-700">Deadline
                    <input v-model="deadlineDate" type="date"
                        class="mt-1 w-fit px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
                </label>
            </div>

            <!-- Interval -->
            <div :class="category === 'recurring' ? 'mb-4' : 'hidden'">
                <label class="text-sm font-medium text-gray-700">Interval
                    <select v-model.trim="interval"
                        class="ml-1 focus:outline-none focus:ring-2 focus:ring-indigo-500 border-gray-300 rounded-md shadow-sm">
                        <option value="daily">Daily</option>
                        <option value="weekly">Weekly</option>
                        <option value="monthly">Monthly</option>
                    </select>
                </label>
            </div>

            <!-- Start Date -->
            <div
                :class="interval === 'weekly' & category === 'recurring' | interval === 'monthly' & category === 'recurring' ? 'mb-4' : 'hidden'">
                <label class="text-sm font-medium text-gray-700">Start Date
                    <input v-model="startDate" type="date"
                        class="mt-1 w-fit px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
                </label>
            </div>

            <!-- Title -->
            <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700">Title
                    <input v-model.trim="title" type="text" required
                        class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
                </label>
            </div>

            <!-- Description -->
            <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700">Description
                    <textarea v-model.trim="description" type="text" required
                        class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
                </label>
            </div>

            <!-- To-do's -->
            <div class="flex flex-col justify-between mb-8">
                <label class="text-sm font-medium text-gray-700">To-do's</label>

                <div class="w-full flex justify-between">
                    <input v-model.trim="newTodo" type="text" placeholder="New to-do"
                        class="mt-1 block w-fill px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
                    <button type="button" @click.prevent="addToDo"
                        class="w-fill h-fit my-auto bg-indigo-600 text-white py-2 px-2 rounded-md hover:bg-indigo-800 transition">Add</button>
                </div>

                <!-- Scrollable To-Do-List -->
                <div class="overflow-x-auto max-h-95 shadow-md p-6">
                    <ul v-for="todo in todoList" :key="todo.id" class="list-disc">
                        <li>{{ todo.text }}</li>
                    </ul>
                </div>
            </div>

            <!-- Utility-Buttons -->
            <div class="w-full flex justify-between">
                <button type="button" @click.prevent="showTaskList"
                    class="w-fit bg-red-700 text-white py-1 px-4 rounded-md hover:bg-red-800 transition">Back</button>

                <button type="reset"
                    class="w-fit bg-indigo-600 text-white py-1 px-4 rounded-md hover:bg-indigo-800 transition">Reset</button>

                <button type="submit"
                    class="w-fit bg-indigo-600 text-white py-1 px-2 rounded-md hover:bg-indigo-800 transition">Submit</button>
            </div>
        </form>
    </div>
</template>

<script setup>
import MessageBox from '@/components/shared/Message-Box.vue';
import { useTasksService } from '@/services/TasksService'
import { ref, watch } from 'vue';

const msg = ref('')
const errorPhrase = 'Something went wrong!'

const { loading, addNewTask } = useTasksService()
const emit = defineEmits(['hideTaskList'])
const mode = ref('')
const priority = ref('')
const topic = ref('')
const category = ref('')
const deadlineDate = ref('')
const interval = ref('')
const startDate = ref('')
const title = ref('')
const description = ref('')
const newTodo = ref('')
const todoList = ref([])
const id = ref(0)

watch(loading, (newVal) => {
    if (newVal) {
        msg.value = "Submitting new task..."
    } else {
        msg.value = ""
    }
})

const addToDo = () => {
    id.value++
    todoList.value.push({ id, text: newTodo.value })
    newTodo.value = ''
}

const submitNewTask = () => {
    const newTask = {
        title: title.value,
        mode: mode.value,
        topic: topic.value,
        category: category.value,
        priority: priority.value,
        deadlineDate: deadlineDate.value || null,
        startDate: startDate.value || null,
        remainingTime: 'NOT IMPLEMENTED YET',
        description: description.value,
        todos: todoList.value,
    }
    console.log(newTask);

    if (addNewTask(newTask)) {
        resetForm()
        msg.value = 'Task successfully added.'
    } else {
        msg.value = 'Something went wrong!'
    }

}

const resetForm = () => {
    mode.value = ''
    priority.value = ''
    topic.value = ''
    category.value = ''
    deadlineDate.value = ''
    interval.value = ''
    startDate.value = ''
    title.value = ''
    description.value = ''
    newTodo.value = ''
    todoList.value = []
}

const showTaskList = () => {
    emit('hideTaskList', false)
}
</script>
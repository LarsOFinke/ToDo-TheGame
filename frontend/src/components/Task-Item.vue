<template>
    <div class="w-full max-w-sm bg-gray-200 rounded-lg shadow-md p-6 mx-auto relative">
        <br>

        <!-- Task-Header -->
        <div class="flex items-center justify-between w-full mb-2">
            <h3 class="text-xl font-bold text-gray-800 mb-2">{{ task.title }}</h3>
            <div class="text-sm font-semibold text-gray-800 mb-2 rounded-lg shadow-md p-1">
                <h4>{{ task.mode }}</h4>
                <h4>{{ task.topic }}</h4>
            </div>
        </div>

        <!-- Task-Info -->
        <div class="flex text-xs mb-4">
            <div class="w-full">
                <label class="font-semibold">Deadline:</label>
                <br>
                <label class="mb-2">{{ task.deadlineDate }}
                    <br>
                    (<label>{{ task.remainingTime }}</label>)
                </label>
            </div>

            <div class="flex float-right">
                <div class="w-full">
                    <label class="text-xs font-semibold">Priority:</label>
                    <p :class="task.priority === 'high' ? 'text-red-600 text-xs font-semibold' : 'text-sm'">{{
                        task.priority }}
                    </p>
                </div>
            </div>
        </div>

        <div class="flex flex-col">
            <!-- Control-Buttons -->
            <div class="w-full flex justify-around">
                <button type="button" @click.prevent="toggleShowDescription(true)"
                    class="w-50 bg-indigo-600 text-white py-1 px-4 rounded-md hover:bg-indigo-800 transition">Description</button>
                <button type="button" @click.prevent="toggleShowDescription(false)"
                    class="w-50 bg-green-600 text-white py-1 px-2 rounded-md hover:bg-green-800 transition">To-Do's</button>
            </div>

            <!-- Task-Description -->
            <div v-if="showDescription">
                <h4 class="font-semibold">Description:</h4>
                <div class="text-sm mb-4 overflow-x-auto h-18">
                    <p class="overflow-y-hidden scrollbar-hide">{{ task.description }}</p>
                </div>
            </div>

            <!-- To-Do-List -->
            <div v-else>
                <h4 class="font-semibold">To-Do's:</h4>
                <div class="text-sm mb-4 overflow-x-auto h-18">
                    <ul v-for="todo in todoList" :key="todo.id">
                        <li :value="todo.id">{{ todo.text }}</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- Utility-Buttons -->
        <div class="mb-2 absolute top-2 right-2">
            <button type="button" @click.prevent="deleteItem"
                class="text-l w-fit bg-red-700 text-white px-2 rounded-md hover:bg-red-800 transition">Delete</button>
        </div>

        <div class="w-full flex justify-around">
            <button type="button" @click.prevent="showItemEdit"
                class="w-fit bg-indigo-600 text-white py-1 px-4 rounded-md hover:bg-indigo-800 transition">Edit</button>
            <button type="button" @click.prevent="closeItem"
                class="w-fit bg-green-600 text-white py-1 px-2 rounded-md hover:bg-green-800 transition">Done!</button>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useTasksService } from '@/services/TasksService'

const emit = defineEmits(['hideItemEdit', 'updateTaskList', 'closeItem'])
const { deleteTask, closeTask } = useTasksService()
const { task } = defineProps({
    task: Object
})
const showDescription = ref(true)

const toggleShowDescription = (toggleOn) => {
    if (toggleOn) {
        showDescription.value = true
    } else {
        showDescription.value = false
    }
}

const showItemEdit = () => {
    emit('hideItemEdit', [false, task])
}

const updateList = () => { emit('updateTaskList', true) }

const deleteItem = async () => {
    await deleteTask(task.id)
    updateList()
    emit('closeItem', 'Item successfully deleted.')
}

const closeItem = async () => {
    await closeTask(task.id)
    updateList()
    emit('closeItem', 'Item successfully closed.')
}

</script>
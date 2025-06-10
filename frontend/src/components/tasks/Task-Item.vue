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
            <!-- ScrollContainer-Control-Buttons -->
            <div class="w-full flex justify-around">
                <button type="button" @click.prevent="toggleShowTodos(true)"
                    :class="showTodos ? 'bg-gray-600 hover:bg-gray-600' : 'bg-gray-400 hover:bg-gray-800'"
                    class="w-50 text-white py-1 px-4 transition">To-Do's</button>
                <button type="button" @click.prevent="toggleShowTodos(false)"
                    :class="showTodos ? 'bg-gray-400 hover:bg-gray-800' : 'bg-gray-600 hover:bg-gray-600'"
                    class="w-50 text-white py-1 px-4 transition">Description</button>
            </div>

            <!-- Task-To-Do's -->
            <div v-if="showTodos" class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-1 mx-auto relative mb-2">
                <div class="text-sm mb-4 overflow-x-auto pl-6 max-h-18">
                    <ul v-for="todo in task.todos" :key="todo.id" class="list-disc">
                        <li :value="todo.id" :class="{ 'line-through': !todo.isOpen }"
                            class="cursor-pointer shadow-md my-3 mr-2" @click.prevent="toggleTodoStatus(todo)">
                            <div class="flex justify-between items-center">
                                <p>{{ todo.text }}</p>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>

            <!-- Task-Description -->
            <div v-else class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-2 mx-auto relative mb-2">
                <div class="text-sm mb-4 overflow-x-auto  max-h-18">
                    <p class="overflow-y-hidden scrollbar-hide">{{ task.description }}</p>
                </div>
            </div>
        </div>

        <!-- Utility-Buttons -->
        <div class="mb-2 absolute top-0 right-0">
            <button type="button" @click.prevent="deleteItem"
                class="text-l w-fit bg-red-700 text-white px-2 rounded-md hover:bg-red-900 transition">Delete</button>
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

const { task } = defineProps({
    task: Object
})
const emit = defineEmits(['hideItemEdit', 'updateTaskList', 'closeItem'])
const { deleteTask, closeTask, closeTodo, openTodo } = useTasksService()
const showTodos = ref(true)

const toggleShowTodos = (toggleOn) => {
    if (toggleOn) {
        showTodos.value = true
    } else {
        showTodos.value = false
    }
}

const showItemEdit = () => {
    emit('hideItemEdit', [false, task])
}

const updateList = () => { emit('updateTaskList', true) }

const toggleTodoStatus = async (todo) => {
    if (todo.isOpen) {
        if (await closeTodo(todo.id)) {
            todo.isOpen = 0
        }
    } else {
        if (await openTodo(todo.id)) {
            todo.isOpen = 1
        }
    }

}

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
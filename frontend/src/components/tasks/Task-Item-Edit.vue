<template>
    <div class="w-full flex flex-col max-w-sm bg-gray-100 rounded-lg shadow-md p-6 mx-auto">
        <h2 class="text-2xl font-bold text-gray-800 mb-4 text-center">Edit</h2>

        <!-- Message-Box -->
        <message-box :msg="msg" :errorPhrase="errorPhrase"></message-box>

        <form @submit.prevent="submitEditedTask">
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
                            ? 'text-red-600 ml-1 focus:outline-none focus:ring-2 focus:ring-indigo-500 border-gray-300 rounded-md shadow-sm'
                            : 'ml-1 focus:outline-none focus:ring-2 focus:ring-indigo-500 border-gray-300 rounded-md shadow-sm'" required>
                        <option value="high">High</option>
                        <option value="medium" class="text-gray-700">Medium</option>
                        <option value="low" class="text-gray-700">Low</option>
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

            <div :class="category === 'timed' ? 'mb-4' : 'hidden'">
                <label class="text-sm font-medium text-gray-700">Deadline
                    <input v-model="deadlineDate" type="date"
                        class="mt-1 w-fit px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
                </label>
            </div>

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

            <div
                :class="interval === 'weekly' & category === 'recurring' | interval === 'monthly' & category === 'recurring' ? 'mb-4' : 'hidden'">
                <label class="text-sm font-medium text-gray-700">Start Date
                    <input v-model="startDate" type="date"
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

            <!-- Task-To-Do's -->
            <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700">To-Do's</label>

                <div class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-2 mx-auto relative mb-2 p-2">
                    <div class="text-sm mb-4 overflow-x-auto  max-h-18">
                        <ul v-for="todo in task.todos" :key="todo.id" class="list-disc pl-6">
                            <li>
                                <div class="flex mb-2">
                                    <input type="text" v-model="todo.text">
                                    <button type="button" @click.prevent="deleteTodo(todo)"
                                        class="w-fit bg-red-700 text-white py-1 px-2 rounded-md hover:bg-red-800 transition">Delete</button>
                                </div>
                            </li>
                        </ul>
                        <ul v-for="todo in newTodoList" :key="todo.id" class="list-disc pl-6">
                            <li>
                                <div class="flex mb-2">
                                    <input type="text" v-model="todo.text">
                                    <button type="button" @click.prevent="deleteNewTodo(todo)"
                                        class="w-fit bg-red-700 text-white py-1 px-2 rounded-md hover:bg-red-800 transition">Delete</button>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>

                <div class="w-full flex justify-between">
                    <input v-model.trim="newTodo" type="text" placeholder="New to-do"
                        class="mt-1 block w-fill px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
                    <button type="button" @click.prevent="addToDo"
                        class="w-fill h-fit my-auto bg-indigo-600 text-white py-2 px-2 rounded-md hover:bg-indigo-800 transition">Add</button>
                </div>
            </div>


            <div class="w-full flex justify-between">
                <button type="button" @click.prevent="showItemEdit"
                    class="w-fit bg-red-700 text-white py-1 px-4 rounded-md hover:bg-red-800 transition">Back</button>

                <button type="reset"
                    class="w-fit bg-indigo-600 text-white py-1 px-4 rounded-md hover:bg-indigo-800 transition">Reset</button>

                <button type="submit"
                    class="w-fit bg-indigo-600 text-white py-1 px-2 rounded-md hover:bg-indigo-800 transition">Edit</button>
            </div>
        </form>
    </div>
</template>

<script setup>
import MessageBox from '@/components/shared/Message-Box.vue';
import { ref, watch } from 'vue';
import { useTasksService } from '@/services/TasksService'

const { task } = defineProps({
    task: Object
})

const msg = ref('')
const errorPhrase = 'Something went wrong!'
const { loading, editTask } = useTasksService()
const emit = defineEmits(['hideItemEdit', 'updateTaskList'])
const mode = ref(task.mode)
const priority = ref(task.priority)
const topic = ref(task.topic)
const category = ref(task.category)
const deadlineDate = ref(task.deadlineDate)
const interval = ref(task.interval)
const startDate = ref(task.startDate)
const title = ref(task.title)
const description = ref(task.description)
const deletedTodos = ref([])
const id = ref(0)
const newTodo = ref('')
const newTodoList = ref([])

watch(loading, (newVal) => {
    if (newVal) {
        msg.value = "Editing task..."
    } else {
        msg.value = ""
    }
})

const showItemEdit = () => {
    emit('hideItemEdit', [true,])
}

const deleteTodo = (todoItem) => {
    deletedTodos.value.push(todoItem)
    const index = task.todos.findIndex(todo => todo.id === todoItem.id);
    if (index !== -1) {
        task.todos.splice(index, 1);
    }
}

const deleteNewTodo = (todoItem) => {
    const index = newTodoList.value.findIndex(todo => todo.id === todoItem.id);
    if (index !== -1) {
        newTodoList.value.splice(index, 1);
    }
}

const addToDo = () => {
    id.value++
    newTodoList.value.push({ id, text: newTodo.value })
    newTodo.value = ''
}

const submitEditedTask = async () => {
    const editedTask = {
        id: task.id,
        title: title.value,
        mode: mode.value,
        category: category.value,
        topic: topic.value,
        priority: priority.value,
        deadlineDate: deadlineDate.value || null,
        startDate: startDate.value || null,
        remainingTime: 'NOT IMPLEMENTED YET',
        description: description.value,
        todos: task.todos,
        deletedTodos: deletedTodos.value,
        newTodoList: newTodoList.value
    }

    if (await editTask(editedTask)) {
        emit('updateTaskList', true)
        msg.value = 'Task successfully updated.'
    } else {
        msg.value = 'Something went wrong!'
    }
}

</script>
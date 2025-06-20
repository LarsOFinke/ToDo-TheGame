<template>
    <div v-if="viewTaskList && !viewItemEdit"
        class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-6 mx-auto relative">
        <!-- Header -->
        <h2 class="text-2xl font-bold text-gray-800 mb-4 text-center">{{ header }}</h2>

        <!-- Message-Box -->
        <message-box :msg="msg" :error-phrase="errorPhrase"></message-box>

        <!-- Utility-Buttons -->
        <div class="flex justify-center mb-4">
            <button type="button" @click.prevent="showTaskForm"
                class="text-l w-fit bg-yellow-600 text-white px-2 py-1 mb-1 rounded-md hover:bg-yellow-800 transition">
                New task
            </button>
        </div>

        <!-- Scrollable Task List -->
        <div class="overflow-x-auto max-h-95">
            <ul class="mb-8">
                <task-item v-for="task in taskList" :key="task.id" :task="task" @hideItemEdit="showItemEdit"
                    @updateTaskList="updateTasks" @closeItem="showMessage"></task-item>
            </ul>
        </div>

        <div v-if="mode === 'team'" class="w-full flex justify-center">
            <button type="button" @click.prevent="showTeamTasks"
                class="w-fit bg-red-700 text-white py-1 px-4 rounded-md hover:bg-red-800 transition">Back</button>
        </div>
    </div>

    <task-item-edit v-else-if="viewItemEdit" :task="selectedTask" @hideItemEdit="showItemEdit"
        @updateTaskList="updateTasks"></task-item-edit>

    <task-form v-else @showTaskForm="showTaskForm"></task-form>
</template>


<script setup>
import MessageBox from '@/components/shared/Message-Box.vue';
import TaskItem from '@/components/tasks/Task-Item.vue';
import TaskItemEdit from '@/components/tasks/Task-Item-Edit.vue';
import TaskForm from '@/components/tasks/Task-Form.vue';
import { ref, onMounted } from 'vue'
import { useTasksService } from '@/services/TasksService';

const { mode, modeId, getAllTasks, tasks } = useTasksService()
const msg = ref('')
const errorPhrase = 'Something went wrong!'
const header = ref('')
const taskList = ref([])
const selectedTask = ref('')
const viewTaskList = ref(true)
const viewItemEdit = ref(false);
const emit = defineEmits(['hideTeamTasks'])

const showTeamTasks = () => {
    emit('hideTeamTasks', [true, 0])
}

const props = defineProps({
    mode: String,
    modeId: Number
})

onMounted(async () => {
    assignMode()
    await fetchTasks()
});

const assignMode = () => {
    mode.value = props.mode
    modeId.value = props.modeId
    header.value = mode.value === 'user' ? 'My Task-List' : 'Team Task-List'
}

const fetchTasks = async () => {
    await getAllTasks(mode.value, modeId.value)
    taskList.value = tasks.value
}

const updateTasks = async () => {
    await getAllTasks(mode.value, modeId.value)
    taskList.value = tasks.value
}

const showTaskForm = async (hideTaskList) => {
    if (hideTaskList) {
        viewTaskList.value = false
    } else {
        assignMode()
        await updateTasks()
        viewTaskList.value = true
    }
}

const showItemEdit = async (hideItemEdit) => {
    if (hideItemEdit[0]) {
        assignMode()
        await updateTasks()
        viewItemEdit.value = false
    } else {
        selectedTask.value = hideItemEdit[1]
        viewItemEdit.value = true
    }
}

const showMessage = (message) => {
    msg.value = message
}

</script>
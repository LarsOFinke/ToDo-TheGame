import { ref } from "vue";
import api from "@/environments/testing-environment";

const loading = ref(false);
const error = ref(null);
const mode = ref('')
const modeId = ref(0)
const tasks = ref([]);

const addNewTask = async (newTask) => {
  loading.value = true;
  error.value = null;
  try {
    await api.post("tasks/add", newTask);
    return true;
  } catch (err) {
    error.value = err.response?.data?.message || "Adding new task failed.";
    return false;
  } finally {
    loading.value = false;
  }
};

const getAllTasks = async (type, id) => {
  loading.value = true;
  error.value = null;
  try {
    const response = await api.post(`tasks/get-all-open-${type}`, { id });
    tasks.value = response.data.tasks;
    error.value = null;
    return true;
  } catch (err) {
    error.value = err.response?.data?.message || "Fetching tasks failed.";
    return false;
  } finally {
    loading.value = false;
  }
};

const editTask = async (editedTask) => {
  loading.value = true;
  error.value = null;
  try {
    await api.post("tasks/edit", editedTask);
    return true;
  } catch (err) {
    error.value = err.response?.data?.message || "Editing task failed.";
    return false;
  } finally {
    loading.value = false;
  }
};

const deleteTask = async (taskId) => {
  loading.value = true;
  error.value = null;
  try {
    await api.post("tasks/delete", { taskId });
    return true;
  } catch (err) {
    error.value = err.response?.data?.message || "Deleting task failed.";
    return false;
  } finally {
    loading.value = false;
  }
};

const closeTask = async (taskId) => {
  loading.value = true;
  error.value = null;
  try {
    await api.post("tasks/close", { taskId });
    return true;
  } catch (err) {
    error.value = err.response?.data?.message || "Closing task failed.";
    return false;
  } finally {
    loading.value = false;
  }
};

const closeTodo = async (todoId) => {
  loading.value = true;
  error.value = null;
  try {
    await api.post("todos/close", { todoId });
    return true;
  } catch (err) {
    error.value = err.response?.data?.message || "Closing todo failed.";
    return false;
  } finally {
    loading.value = false;
  }
};

const openTodo = async (todoId) => {
  loading.value = true;
  error.value = null;
  try {
    await api.post("todos/open", { todoId });
    return true;
  } catch (err) {
    error.value = err.response?.data?.message || "Opening todo failed.";
    return false;
  } finally {
    loading.value = false;
  }
};

export function useTasksService() {
  return {
    loading,
    error,
    mode,
    modeId,
    tasks,
    addNewTask,
    getAllTasks,
    editTask,
    deleteTask,
    closeTask,
    closeTodo,
    openTodo,
  };
}

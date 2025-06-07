import { ref } from "vue";
import api from "@/environments/testing-environment";

const loading = ref(false);
const error = ref(null);
const tasks = ref([]);

export function useTasksService() {
  const addNewTask = async (newTask) => {
    loading.value = true;
    error.value = null;
    try {
      console.log("Attempting to add new Task: ", newTask);
      await api.post("tasks/add", newTask);
      return true;
    } catch (err) {
      error.value = err.response?.data?.message || "Adding new task failed.";
      return false;
    } finally {
      loading.value = false;
    }
  };

  const getAllTasks = async () => {
    await api
      .get("tasks/get-all")
      .then((data) => {
        tasks.value = data.data.tasks;
        console.log(tasks.value);
        return true;
      })
      .catch((err) => {
        console.log(err);
        return false;
      })
      .finally(() => {
        loading.value = false;
      });
  };

  const editTask = async (editedTask) => {
    loading.value = true;
    error.value = null;
    try {
      console.log("Attempting to edit Task:", editedTask);
      await api.post("tasks/edit", editedTask);
      return true;
    } catch (err) {
      error.value = err.response?.data?.message || "Editing task failed.";
      return false;
    } finally {
      loading.value = false;
    }
  };

  return {
    loading,
    error,
    tasks,
    addNewTask,
    getAllTasks,
    editTask,
  };
}

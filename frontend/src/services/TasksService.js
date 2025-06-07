import { ref } from "vue";
import api from "@/environments/testing-environment";

const loading = ref(false);
const error = ref(null);

export function useTasksService() {
  const addNewTask = async (newTask) => {
    loading.value = true;
    error.value = null;
    try {
      console.log("Attempting to add new Task: ", newTask);
      await api.post("tasks/add", newTask);
      return true;
    } catch (err) {
      error.value =
        err.response?.data?.message ||
        "Adding new task failed.";
      return false;
    } finally {
      loading.value = false;
    }
  };


  const editTask = async (editedTask) => {
    loading.value = true;
    error.value = null;
    try {
      console.log("Attempting to edit Task:", editedTask);
      await api.post("tasks/edit", editedTask);
      return true;
    } catch (err) {
      error.value =
        err.response?.data?.message ||
        "Editing task failed.";
      return false;
    } finally {
      loading.value = false;
    } 
  }

  return {
    loading,
    error,
    addNewTask,
    editTask,
  };
  
}

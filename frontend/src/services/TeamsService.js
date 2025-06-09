import { ref } from "vue";
import api from "@/environments/testing-environment";

const loading = ref(false);
const error = ref(null);

const createNewTeam = async (newTeam) => {
  loading.value = true;
  try {
    const response = await api.post("teams/create", newTeam);
    if (response.data.success) {
      return true;
    } else {
      return false;
    }
  } catch (err) {
    error.value = err.response?.data?.message || "Creating new team failed.";
    return false;
  } finally {
    loading.value = false;
  }
};

export function useTeamsService() {
  return {
    loading,
    createNewTeam,
  };
}

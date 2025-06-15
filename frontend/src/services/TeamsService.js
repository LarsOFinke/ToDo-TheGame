import { ref } from "vue";
import api from "@/environments/testing-environment";

const loading = ref(false);
const error = ref(null);
const teams = ref([]);

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

const getAllTeamsNotJoined = async (userId) => {
  loading.value = true;
  try {
    const response = await api.post("teams/get-all-team-not-joined", {
      userId,
    });
    if (response.data.success) {
      teams.value = response.data.teams;
      return true;
    } else {
      return false;
    }
  } catch (err) {
    error.value = err.response?.data?.message || "Fetching teams failed.";
    return false;
  } finally {
    loading.value = false;
  }
};

const getTeamsForUser = async (id) => {
  loading.value = true;
  try {
    const response = await api.post("teams/get-all-team-user", { id });
    if (response.data.success) {
      teams.value = response.data.teams;
      return true;
    } else {
      return false;
    }
  } catch (err) {
    error.value = err.response?.data?.message || "Fetching teams failed.";
    return false;
  } finally {
    loading.value = false;
  }
};

export function useTeamsService() {
  return {
    loading,
    teams,
    createNewTeam,
    getTeamsForUser,
    getAllTeamsNotJoined,
  };
}

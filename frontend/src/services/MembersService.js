import { ref } from "vue";
import api from "@/environments/testing-environment";

const loading = ref(false);
const error = ref(null);
const members = ref([]);
const memberCount = ref(0)

const addNewMember = async (newMember) => {
  loading.value = true;
  try {
    const response = await api.post("members/add", newMember);
    if (response.data.success) {
      return true;
    } else {
      return false;
    }
  } catch (err) {
    error.value = err.response?.data?.message || "Adding new member failed.";
    return false;
  } finally {
    loading.value = false;
  }
};

const fetchMembersForTeam = async (id) => {
  loading.value = true;
  try {
    const response = await api.post("members/get-all-members-for-team", { id });
    if (response.data.success) {
      members.value = response.data.members;
      return true;
    } else {
      return false;
    }
  } catch (err) {
    error.value =
      err.response?.data?.message || "Fetching members for team failed.";
    return false;
  } finally {
    loading.value = false;
  }
};

const fetchMemberCountForTeam = async (id) => {
  loading.value = true;
  try {
    const response = await api.post("members/get-member-count-for-team", {
      id,
    });
    if (response.data.success) {
      memberCount.value = response.data.memberCount;
      return true;
    } else {
      return false;
    }
  } catch (err) {
    error.value =
      err.response?.data?.message || "Fetching member count for team failed.";
    return false;
  } finally {
    loading.value = false;
  }
};

export function useMembersService() {
  return {
    loading,
    members,
    memberCount,
    addNewMember,
    fetchMembersForTeam,
    fetchMemberCountForTeam,
  };
}

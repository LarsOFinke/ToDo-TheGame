import { ref } from "vue";
import api from "@/environments/testing-environment";

const user = ref(null);
const userId = ref(0);
const isAuthenticated = ref(false);
const loading = ref(false);
const error = ref(null);

const login = async (username, password) => {
  loading.value = true;
  error.value = null;
  try {
    const response = await api.post("auth/login", { username, password });
    console.log(response.data);
    if (response.data.success) {
      user.value = response.data.username;
      console.log(user.value);
      userId.value = response.data.userId;
      console.log(userId.value);
      isAuthenticated.value = true;
    } else {
      isAuthenticated.value = false;
    }
  } catch (err) {
    error.value = err.response?.data?.message || "Login failed.";
    isAuthenticated.value = false;
  } finally {
    loading.value = false;
  }
};

const register = async (username, password) => {
  loading.value = true;
  error.value = null;
  try {
    const response = await api.post("auth/register", { username, password });
    user.value = response.data.user;
    return true;
  } catch (err) {
    error.value = err.response?.data?.message || "Registration failed.";
    return false;
  } finally {
    loading.value = false;
  }
};

const clearSession = () => {
  api.get("auth/clear-session").then(() => {
    user.value = null;
    isAuthenticated.value = false;
  });
};

export function useAuthService() {
  return {
    user,
    isAuthenticated,
    loading,
    error,
    register,
    login,
    clearSession,
  };
}

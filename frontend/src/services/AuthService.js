// services/AuthService.js
import { ref } from "vue";
import api from "@/environments/testing-environment";

// ✅ Declare shared reactive state at module level
const user = ref(null);
const isAuthenticated = ref(false);
const loading = ref(false);
const error = ref(null);

// ✅ Use regular functions that act on shared state
const login = async (username, password) => {
  loading.value = true;
  error.value = null;
  try {
    const response = await api.post("auth/login", { username, password });
    user.value = response.data.user;
    isAuthenticated.value = true;
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

// ✅ Export shared state and actions directly
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

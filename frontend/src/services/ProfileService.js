import { ref } from "vue";
import api from "@/environments/testing-environment";

const loading = ref(false);
const error = ref(null);

const xxx = async () => {
    loading.value = true;
  try {
    const response = await api.post("", {  });
    if (response.data.success) {

    } else {

    }
  } catch (err) {
    error.value = err.response?.data?.message || "XXX failed.";

  } finally {
    loading.value = false;
  }
};

export function useProfileService() {
  return {
    xxx,
  };
}

<template>
    <div class="w-full max-w-sm bg-white rounded-lg shadow-md p-6 mx-auto">
        <h2 class="text-2xl font-semibold text-gray-800 mb-4 text-center">Profile</h2>

        <!-- Message-Box -->
        <message-box :msg="msg" :errorPhrase="errorPhrase"></message-box>

        <profile-item v-if="!editMode" @showEditMode="toggleEditMode"></profile-item>
        <profile-form v-else @showEditMode="toggleEditMode"></profile-form>
    </div>
</template>

<script setup>
import MessageBox from '@/components/shared/Message-Box.vue'
import ProfileForm from '@/components/Profile-Form.vue'
import ProfileItem from '@/components/Profile-Item.vue'
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthService } from '@/services/AuthService'

const router = useRouter();
const { isAuthenticated } = useAuthService()
const msg = ref('')
const errorPhrase = 'Something went wrong!'
const editMode = ref(false)

onMounted(async () => {
    if (!isAuthenticated.value) {
        router.replace('/');
    }
});

const toggleEditMode = (activateEditMode) => {
    if (activateEditMode) {
        editMode.value = true
    } else {
        editMode.value = false
    }
}

</script>
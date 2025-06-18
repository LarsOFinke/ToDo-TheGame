<template>
    <tr>
        <td>{{ member.username }}</td>
        <!--  -->
        <td>
            <select v-model="selectedRole">
                <option v-for="role in availableRoles" :key="role" :value="role"
                    :disabled="props.isTeamAdmin.value ? false : true">
                    {{ role }}
                </option>
            </select>
        </td>
    </tr>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
    isTeamAdmin: Boolean,
    member: Object,
})
const selectedRole = ref(props.member.teamRole)
const availableRoles = ['leader', 'officer', 'member']
</script>
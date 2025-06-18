<template>
    <tr>
        <td>{{ member.username }}</td>

        <!-- Member-Team-Role(-Selection) -->
        <td v-if="isTeamAdmin">
            <select v-model="assignedRole">
                <option v-for="role in availableRoles" :key="role" :value="role">
                    {{ role }}
                </option>
            </select>
        </td>
        <td v-else>
            {{ assignedRole }}
        </td>
    </tr>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
    isTeamAdmin: Boolean,
    member: Object,
})
const assignedRole = ref(props.member.teamRole)
const availableRoles = ['leader', 'officer', 'member']
</script>
<template>
    <tr>
        <td>{{ member.username }}</td>
        <!--  -->
        <td>
            <select v-model="selectedRole">
                <option v-for="role in availableRoles" :key="role" :value="role">
                    {{ role }}
                </option>
            </select>
        </td>
    </tr>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
    member: Object,
})
const selectedRole = ref(props.member.teamRole)
const availableRoles = ['leader', 'member', 'candidate']
</script>
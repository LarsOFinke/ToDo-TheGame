<template>
    <h3 class="text-lg mb-2 font-semibold">Member-List</h3>

    <div class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-1 mx-auto relative mb-2">

        <div class="text-sm mb-2 overflow-x-auto max-h-24">
            <table class="w-full border-1">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Role</th>
                    </tr>
                </thead>
                <tbody>
                    <members-item v-for="member in memberList" :key="member.id" :member="member"
                        :isTeamAdmin="isTeamAdmin" />
                </tbody>
            </table>
        </div>
    </div>
</template>

<script setup>
import MembersItem from '@/components/members/Members-Item.vue';
import { ref, onMounted } from 'vue'

const props = defineProps({
    userId: Number,
    memberList: Array,
    member: Object,
})
const isTeamAdmin = ref(false)

onMounted(() => {
    for (let member in props.memberList.value) {
        if (member.id === userId.value && member.teamRole === 'leader' | 'officer') {
            isTeamAdmin.value = true
        }
    }
})
</script>
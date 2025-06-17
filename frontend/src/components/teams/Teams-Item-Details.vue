<template>
    <div class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-2 mx-auto relative mb-2">
        <members-list :memberList="memberList"></members-list>
    </div>
</template>

<script setup>
import MembersList from '@/components/members/Members-List.vue';

const props = defineProps({
    memberList: Array,
})
</script>
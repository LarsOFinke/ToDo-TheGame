<template>
    <h3 class="text-lg mb-2 font-semibold">Member-List</h3>

    <div class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-1 mx-auto relative mb-2">

        <div class="text-sm mb-2 overflow-x-auto max-h-24">
            <table class="w-full border-1">
                <tr>
                    <th>Name</th>
                    <th>Role</th>
                </tr>
                <tr v-for="member in memberList">
                    <members-item :member="member"></members-item>
                </tr>
            </table>
        </div>
    </div>
</template>

<script setup>
import MembersItem from '@/components/members/Members-Item.vue';

const props = defineProps({
    memberList: Array,
})
</script>
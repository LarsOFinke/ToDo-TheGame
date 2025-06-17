<template>
    <td>{{ member.username }}</td>
    <td>{{ member.teamRole }}</td>
</template>

<script setup>

const props = defineProps({
    member: Object,
})
</script>
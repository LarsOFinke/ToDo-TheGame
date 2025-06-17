<template>
    <li class="mb-1">{{ member.username }} | {{ member.teamRole }}</li>
</template>

<script setup>

const props = defineProps({
    member: Object,
})
</script>
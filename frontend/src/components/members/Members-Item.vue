<template>
    <li class="mb-1">{{ member.username }}</li>
</template>

<script setup>

const props = defineProps({
    member: Object,
})
</script>
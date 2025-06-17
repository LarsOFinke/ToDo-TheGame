<template>
    <tr>
        <td>{{ member.username }}</td>
        <td>{{ member.teamRole }}</td>
    </tr>
</template>

<script setup>

const props = defineProps({
    member: Object,
})
</script>
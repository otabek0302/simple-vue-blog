<style scoped>
.card {
  width: 100%;
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  background: #ffffff;
  overflow: hidden;
}

.card__header,
.card__footer {
  padding: 12px 16px;
  background: #fafafa;
  border-bottom: 1px solid #eaeaea;
}

.card__footer {
  border-top: 1px solid #eaeaea;
  border-bottom: none;
}

.card__body {
  padding: 16px;
}
</style>

<template>
  <section :class="['card', cardClass]">
    <header v-if="$slots.header" class="card__header">
      <slot name="header" />
    </header>
    <div class="card__body">
      <slot />
    </div>
    <footer v-if="$slots.footer" class="card__footer">
      <slot name="footer" />
    </footer>
  </section>
  
</template>

<script>
export default {
  name: "Card",
  props: {
    cardClass: {
      type: String,
      default: "",
    },
  },
};
</script>



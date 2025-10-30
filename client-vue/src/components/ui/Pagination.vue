<style scoped>
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;
  margin: 32px 0;
  flex-wrap: wrap;
}
.pagination__btn {
  min-width: 40px;
  height: 40px;
  padding: 0 12px;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  background: #fff;
  color: #374151;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}
.pagination__btn:hover:not(:disabled) {
  background: #f3f4f6;
  border-color: #3b82f6;
  color: #3b82f6;
}
.pagination__btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
.pagination__btn--active {
  background: #3b82f6;
  border-color: #3b82f6;
  color: #fff;
}
.pagination__btn--active:hover {
  background: #2563eb;
}
.pagination__info {
  margin: 0 8px;
  font-size: 14px;
  color: #6b7280;
}
@media (max-width: 640px) {
  .pagination {
    gap: 4px;
  }
  .pagination__btn {
    min-width: 36px;
    height: 36px;
    padding: 0 8px;
    font-size: 12px;
  }
  .pagination__info {
    width: 100%;
    text-align: center;
    margin: 8px 0;
  }
}
</style>

<template>
  <div v-if="totalPages > 1" class="pagination">
    <button
      class="pagination__btn"
      :disabled="currentPage === 1"
      @click="$emit('pageChange', currentPage - 1)"
      aria-label="Previous page"
    >
      <i class="fas fa-chevron-left"></i>
    </button>

    <template v-for="page in visiblePages" :key="page">
      <button
        v-if="page !== '...'"
        class="pagination__btn"
        :class="{ 'pagination__btn--active': page === currentPage }"
        @click="$emit('pageChange', page)"
      >
        {{ page }}
      </button>
      <span v-else class="pagination__info">...</span>
    </template>

    <button
      class="pagination__btn"
      :disabled="currentPage === totalPages"
      @click="$emit('pageChange', currentPage + 1)"
      aria-label="Next page"
    >
      <i class="fas fa-chevron-right"></i>
    </button>

    <span class="pagination__info">
      Page {{ currentPage }} of {{ totalPages }}
    </span>
  </div>
</template>

<script>
export default {
  name: "Pagination",
  props: {
    currentPage: {
      type: Number,
      required: true,
      default: 1,
    },
    totalPages: {
      type: Number,
      required: true,
      default: 0,
    },
  },
  computed: {
    visiblePages() {
      const pages = [];
      const total = this.totalPages;
      const current = this.currentPage;

      if (total <= 7) {
        // Show all pages if 7 or fewer
        for (let i = 1; i <= total; i++) {
          pages.push(i);
        }
      } else {
        // Always show first page
        pages.push(1);

        if (current <= 4) {
          // Near the start
          for (let i = 2; i <= 5; i++) {
            pages.push(i);
          }
          pages.push("...");
          pages.push(total);
        } else if (current >= total - 3) {
          // Near the end
          pages.push("...");
          for (let i = total - 4; i <= total; i++) {
            pages.push(i);
          }
        } else {
          // In the middle
          pages.push("...");
          for (let i = current - 1; i <= current + 1; i++) {
            pages.push(i);
          }
          pages.push("...");
          pages.push(total);
        }
      }

      return pages;
    },
  },
  emits: ["pageChange"],
};
</script>


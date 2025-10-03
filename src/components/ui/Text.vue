<style scoped>
.text-primary {
  color: #0057ff;
}
.text-title {
  color: #010101;
}

.text-subtitle {
  color: #323232;
}

.text-text {
  color: #555555;
}

.text-link {
  color: #0057ff;
}

.text-error {
  color: #dc3545;
}

.text-warning {
  color: #ffc107;
}

.text-success {
  color: #28a745;
}

.text-white {
  color: #ffffff;
}

.text-center {
  text-align: center;
}

.text-left {
  text-align: left;
}

.text-right {
  text-align: right;
}

.text-justify {
  text-align: justify;
}

.text-uppercase {
  text-transform: uppercase;
}

.text-lowercase {
  text-transform: lowercase;
}

.text-capitalize {
  text-transform: capitalize;
}

.text-bold {
  font-weight: 600;
}

.text-normal {
  font-weight: 400;
}

.text-light {
  font-weight: 300;
}

.text-italic {
  font-style: italic;
}

.text-underline {
  text-decoration: underline;
}

.text-no-decoration {
  text-decoration: none;
}
</style>

<template>
  <component :is="type" :class="classes">
    <span v-if="displayText" v-html="displayText"></span>
    <slot v-else></slot>
  </component>
</template>

<script>
export default {
  name: "Text",
  props: {
    textClass: {
      type: String,
      default: "",
    },
    type: {
      type: String,
      default: "p",
      validator: (value) => ["p", "h1", "h2", "h3", "h4", "h5", "h6", "span", "div", "label"].includes(value),
    },
    variant: {
      type: String,
      default: "",
      validator: (value) => ["primary", "title", "subtitle", "text", "link", "error", "warning", "success", "white", ""].includes(value),
    },
    align: {
      type: String,
      default: "",
      validator: (value) => ["left", "center", "right", "justify", ""].includes(value),
    },
    transform: {
      type: String,
      default: "",
      validator: (value) => ["uppercase", "lowercase", "capitalize", ""].includes(value),
    },
    weight: {
      type: String,
      default: "",
      validator: (value) => ["bold", "normal", "light", ""].includes(value),
    },
    textStyle: {
      type: String,
      default: "",
      validator: (value) => ["italic", "underline", "no-decoration", ""].includes(value),
    },
    text: {
      type: String,
      default: "",
    },
  },
  computed: {
    classes() {
      const classes = [];

      // Add custom class
      if (this.textClass) {
        classes.push(this.textClass);
      }

      // Add variant classes
      if (this.variant) {
        classes.push(`text-${this.variant}`);
      }

      // Add alignment classes
      if (this.align) {
        classes.push(`text-${this.align}`);
      }

      // Add transform classes
      if (this.transform) {
        classes.push(`text-${this.transform}`);
      }

      // Add weight classes
      if (this.weight) {
        classes.push(`text-${this.weight}`);
      }

      // Add style classes
      if (this.textStyle) {
        classes.push(`text-${this.textStyle}`);
      }

      return classes;
    },
    displayText() {
      return this.text;
    },
  },
};
</script>

<script>
  /**
   * @type {string}
  */
  export let textTag = 'p';
  export let textColor = '' ;
</script>

<svelte:element this={textTag}
  style:color= {textColor === 'grey' ? 'var(--color-text-medium)' : textColor === 'blue' ? 'var(--color-primary)' : 'var(--color-text-dark)'}
  class='text {$$props.class}'
>
  <slot/>
</svelte:element>
  
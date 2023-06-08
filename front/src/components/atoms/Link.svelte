<script>
  /**
   * @type {string}
  */
  export let linkUrl = '#';
</script>

<a href="{linkUrl}"
  on:click
  class="link {$$props.class}">          
    <slot/>
</a>

<style>
  .link{
    font-family: var(--font-family-primary);
    font-size: var(--font-size-regular);
    color: var(--color-text-dark);
    text-decoration: none;
    display: inline-block;
  }

  .link--current{
    color: var(--color-primary);
    text-decoration: underline;
    text-underline-offset: 5px;
  }
</style>
  
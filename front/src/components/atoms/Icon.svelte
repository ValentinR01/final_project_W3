<script>
  /**
   * @type {string}
  */
  export let name = ''
  export let color = 'currentColor'
  export let width = "30";
  export let height = "30";
</script>

<div style='width:{width}px; height:{height}px'>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    aria-labelledby={name}
    role="presentation"
    class={$$props.class}
    viewBox="0 0 30 30"
    preserveAspectRatio="xMidYMid meet"
  >
    <title id={name} lang="en">{`${name} icon`}</title>
    <g fill={color}>
      <slot />
    </g>
  </svg>
</div>

<style>
  .modal__icon{
    position: absolute;
    right: 40px;
    top: 40px;
  }
</style>
<script>
  import Icon from "../../atoms/Icon.svelte";
</script>

<div class='video-action'>
  <Icon name='video-action' class='block-center' width=50 height=50>
    <slot name='icon' />
  </Icon>
  <p class='video-action__text text-preset-3 text--uppercase text-center'>
    <slot name='text' />
  </p>
</div>

<style>
  .video-action{
    width: 380px;
    padding: var(--spacing-4);
    background-color: var(--color-background-tercary);
    border: 1px solid var(--color-border);
    border-radius: var(--card-radius);
  }

  .video-action__text{
    margin-top: var(--spacing-3);
  }
</style>
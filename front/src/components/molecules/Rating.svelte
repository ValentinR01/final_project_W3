<script>
  import SquareIcon from "../../assets/icons/SquareIcon.svelte";
  import Icon from "../atoms/Icon.svelte";
  import Text from "../atoms/Text.svelte";

  /**
   * @type {number}
  */
  export let rate = 0;
</script>

<div class='rating-container'>
    {#if rate < 1}
      <Text textTag='p' class='text-preset-4'>N/A</Text>
    {:else }
      {#each {length: 4} as star, i}
        <Icon name="square" width="10" height="10" color='{i < rate ? 'var(--color-primary)' : 'var(--grey)' }'>
          <SquareIcon />
        </Icon>
      {/each}
    {/if }
</div>

<style>
  .rating-container{
    display: flex;
    column-gap: var(--spacing-1);
  }
</style>
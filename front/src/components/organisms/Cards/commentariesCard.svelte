<script>
  import Margin from "../../atoms/Margin.svelte";
  import Text from "../../atoms/Text.svelte";
  import CommentaryCard from "../../molecules/cards/CommentaryCard.svelte";
  import CommentaryForm from "../Forms/CommentaryForm.svelte";

  /**
   * @type { any }
  */
  export let data;

</script>

<div class='card card-commentaries block-center'>
  <Margin marginBottom='var(--spacing-2)'>
    <Text
      textTag='h2'
      class='text-preset-2 text--uppercase'
    >
      Commentaires
    </Text>
  </Margin>

  <CommentaryCard>
    <span slot='name'>{data.users[1].fullname}</span>
    <span slot='job'>{data.users[1].domain}</span>
    <span slot='date'> 12/06/2023 </span>
    <span slot='comment'> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. </span>
  </CommentaryCard>

  <CommentaryCard>
    <span slot='name'>{data.users[1].fullname}</span>
    <span slot='job'>{data.users[1].domain}</span>
    <span slot='date'> 12/06/2023 </span>
    <span slot='comment'> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. </span>
  </CommentaryCard>

  <CommentaryForm />
</div>

<style>
  .card-commentaries{
    margin: var(--spacing-3) auto;
    display: flex;
    flex-wrap: wrap;
    row-gap: var(--spacing-2);
    max-height: 100%;
  }
</style>
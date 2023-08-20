<script>
  import Margin from "../../components/atoms/Margin.svelte";
  import CommentaryCard from "../../components/molecules/cards/CommentaryCard.svelte";
  import CommentaryForm from "../../components/organisms/Forms/CommentaryForm.svelte";
</script>

<Margin marginBottom='var(--spacing-2)'>
  <CommentaryCard>
    <span slot='name'><!--{data.users[1].fullname}--> Derek Tom</span>
    <span slot='job'><!--{data.users[1].domain}-->Traducteur</span>
    <span slot='date'> 12/06/2023 </span>
    <span slot='comment'> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. </span>
  </CommentaryCard>
</Margin>

<CommentaryForm />

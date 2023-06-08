<script>
  import SearchIcon from "../../assets/icons/SearchIcon.svelte";
  import Button from "../../stories/Button.svelte";
  import Icon from "../atoms/Icon.svelte";
  import Input from "../atoms/Input.svelte";
</script>

<div class='searchbar'>
    <Input />
    <Button>
      <Icon name="searchbar">
        <SearchIcon/>
      </Icon>
    </Button>
</div>